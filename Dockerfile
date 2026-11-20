FROM ruby:3.4-alpine

# Install system dependencies for Ruby
RUN apk add --no-cache \
      build-base \
      git \
      openssl-dev \
      libxml2-dev \
      libxslt-dev \
      openssh-client \
      file \
      curl \
      make \
      g++

# Create working directory
WORKDIR /app

# Copy Gemfile
COPY Gemfile ./

# Install bundle (without deployment mode for Docker build)
RUN gem install bundler:2.5.4 --no-document && \
    bundle install --jobs=3 --retry=3

# Create necessary directories
RUN mkdir -p \
      /app/_layouts \
      /app/styles \
      /app/assets \
      /app/images \
      /app/_includes \
      /app/_data

# Copy source files
COPY . .

# Create a standalone Jekyll build context
RUN mkdir -p /jekyll-build && \
    cp Gemfile /jekyll-build/ && \
    cp _config.yml /jekyll-build/ && \
    cp -r _layouts /jekyll-build/ && \
    cp -r styles /jekyll-build/ && \
    cp -r images /jekyll-build/ 2>/dev/null || true

# Generate compatible Gemfile.lock for jekyll-build
RUN cd /jekyll-build && \
    echo 'source "https://rubygems.org"' > Gemfile.lock && \
    echo 'gem "jekyll", "~> 4.3.0"' >> Gemfile.lock && \
    echo 'gem "github-pages", "~> 233.0"' >> Gemfile.lock && \
    echo 'gem "jekyll-kramdown", "~> 0.8.0"' >> Gemfile.lock && \
    echo 'gem "jekyll-paginate", "~> 1.1.0"' >> Gemfile.lock && \
    echo 'gem "jekyll-sitemap", "~> 1.6.0"' >> Gemfile.lock && \
    echo 'gem "jekyll-tidy", "~> 1.2.0"' >> Gemfile.lock

# Install gems in build context
RUN cd /jekyll-build && \
    bundle install --jobs=3 --retry=3 && \
    cd /app

# Set default command
CMD ["bundle", "exec", "jekyll", "build"]
